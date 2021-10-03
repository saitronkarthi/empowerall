
'use strict';
var AWS = require('aws-sdk'),
    transcoder = new AWS.ElasticTranscoder({
        apiVersion: '2012-09-25'
    });
exports.handler = (event, context, callback) => {
    let fileName = event.Records[0].s3.object.key;
    console.log("FileName:"+fileName);
    var srcKey =  decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, " "));
    console.log("FileName2:"+srcKey);
    var newKey = fileName.split('.')[0];
    console.log('A new video has been uploaded for process:', fileName);
transcoder.createJob({
     PipelineId: process.env.PIPELINE_ID,
     Input: {
      Key: srcKey,
      FrameRate: 'auto',
      Resolution: 'auto',
      AspectRatio: 'auto',
      Interlaced: 'auto',
      Container: 'auto'
     },
     Output: {
      Key: getOutputName(fileName),
      ThumbnailPattern: '',
      PresetId: '1351620000001-300040',
      Rotate: 'auto'
     }
    }, function(err, data){
        if(err){
            console.log('Error occured:',err)
        }else{
            console.log('Video conversion done');
        }
     callback(err, data);
    });
};
function getOutputName(srcKey){
 let baseName = srcKey.replace('video/','');
 let withOutExtension = removeExtension(baseName);
 return 'audio/' + withOutExtension + '.mp3';
}
function removeExtension(srcKey){
    let lastDotPosition = srcKey.lastIndexOf(".");
    if (lastDotPosition === -1) return srcKey;
    else return srcKey.substr(0, lastDotPosition);
}
