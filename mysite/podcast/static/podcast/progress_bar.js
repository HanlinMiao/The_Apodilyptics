var canvasWidth = 300
var audioEl = document.getElementById("audio")
var canvas = document.getElementById("progress").getContext('2d')
var ctrl = document.getElementById('audioControl')

audioEl.addEventListener('loadedmetadata', function() {
  var duration = audioEl.duration
  var currentTime = audioEl.currentTime
  document.getElementById("duration").innerHTML = convertElapsedTime(duration)
  document.getElementById("current-time").innerHTML = convertElapsedTime(currentTime)
  canvas.fillStyle = "#D3D3D3";
  canvas.fillRect(0, 0, canvasWidth, 50);
});

function updateBar(e){
	var x = e.pageX - thisoffsetLeft;
	var xconvert = x/300;
	var finalx = (xconvert).toFixed(30);
	audioEl.currentTime = finalx*duration;
	canvas.clearRect(0, 0, canvasWidth, 50)
	canvas.fillStyle = "#D3D3D3";
  	canvas.fillRect(0, 0, canvasWidth, 50)
  	var currentTime = audioEl.currentTime
  	var duration = audioEl.duration
  	if (currentTime === duration) {
    	ctrl.innerHTML = "Play"
  	}
  	document.getElementById("current-time").innerHTML = convertElapsedTime(currentTime)
  	var percentage = currentTime / duration
  	var progress = (canvasWidth * percentage)
  	canvas.fillStyle = "#A9A9A9"
  	canvas.fillRect(0, 0, progress, 50)
}

function togglePlaying() {

  var play = ctrl.innerHTML === 'Play'
  var method

  if (play) {
    ctrl.innerHTML = 'Pause'
    method = 'play'
  } else {
    ctrl.innerHTML = 'Play'
    method = 'pause'
  }

  audioEl[method]()

}

function updateBar() {
  canvas.clearRect(0, 0, canvasWidth, 50)
  canvas.fillStyle = "#D3D3D3";
  canvas.fillRect(0, 0, canvasWidth, 50)
  
  var currentTime = audioEl.currentTime
  var duration = audioEl.duration
  
  if (currentTime === duration) {
    ctrl.innerHTML = "Play"
  }
  
  document.getElementById("current-time").innerHTML = convertElapsedTime(currentTime)
  
  var percentage = currentTime / duration
  var progress = (canvasWidth * percentage)
  canvas.fillStyle = "#A9A9A9"
  canvas.fillRect(0, 0, progress, 50)
}

function convertElapsedTime(inputSeconds) {
  var seconds = Math.floor(inputSeconds % 60)
  if (seconds < 10) {
    seconds = "0" + seconds
  }
  var minutes = Math.floor(inputSeconds / 60)
  return minutes + ":" + seconds
}