//const gameStart = document.getElementById('startGame')
const resultEndMessage = document.querySelector(".end-message");
const fineScoreResult = document.querySelector(".fine-score-result");
const getWordSize = document.querySelector("#validationCustom05");
const TimeLeftCounter = document.querySelector(".Time-left");
const scoreYouGot = document.querySelector(".score_result");
const restartGameToPlayButton = document.querySelector('.reset_button');
const resetOperator = document.querySelector(".resetOperator");
const selectedWordSize = document.querySelector(".selected-word-size");
const ourFieldAnswer = document.querySelector(".answer-input");
const problemElement = document.querySelector(".problem");
const reamingAnswer = document.querySelector(".reaming-answer");
// ---------Form data Input-------------------
const word_sizeData = document.querySelector('#id_word_size')
const score_Data = document.querySelector('#id_score')
const pointData = document.querySelector('#id_point')
const rankedData = document.querySelector('#id_ranked')  
//json 
var jsonData = JSON.parse(document.getElementById('element_id').textContent);
console.log(jsonData)
//global variables
let state = { timeLeft: 0, score: 1, timer: 10, isPlaying: 1 }

//return random number
function randInt(low, high) {
    const rndDec = Math.random();
    return Math.floor(rndDec * (high - low + 1) + low);
}
//game luncher
function gameLaunch(){
    document.getElementById('start2').style.display='none';
    //document.getElementById('ownGameScore').style.display='none';
    document.getElementById('toggle2').style.display='block';
    starter();
}

//starter
function starter() {

    init();
    const TimeCounterStart = setInterval(counter, 1000);
    const startGameTimer = setInterval(checkStates, 1000);

    function checkStates() {
            if (state.timer > 0 && state.isPlaying === 1) {
                state.isPlaying = 1;
            }else if (state.timer === 0 && state.isPlaying === 0) {
                //clearInterval-TimeCounterStart
                
                clearInterval(TimeCounterStart);
                //overlay result
                document.body.classList.add("overlay-is-open");
                resultEndMessage.textContent = "Time is up!!.";
                fineScoreResult.innerHTML = state.score;
                score_Data.value = state.score;
                let WordSize= Number(getWordSize.options[document.getElementById('validationCustom05').selectedIndex].value)
                pointData.value = state.score * WordSize;
                clearInterval(startGameTimer);
            } 
    }
}


//time counter
function counter() {
    if (state.timer > 0) {
        state.timer--;
        state.isPlaying = 1;
        TimeLeftCounter.innerHTML = state.timer;
    } 
    else if (state.timer === 0) {
        state.isPlaying = 0;
    }
}

restartGameToPlayButton.addEventListener('click', restartGameToPlay);
resetOperator.addEventListener('click', resetOperatorGameToPlay); 

function restartGameToPlay() {
    //remove overlay
    document.body.classList.remove("overlay-is-open");
    state.score = 0;
    state.timer = 10;
    scoreYouGot.innerHTML = state.score;
    //re-starter
    starter();

}
//remove overlay-is-open css from body
//reset all classes, variables, and input fields
function resetOperatorGameToPlay(){
    document.body.classList.remove("overlay-is-open");
    document.getElementById('start2').style.display='block';
    //document.getElementById('ownGameScore').style.display='block';
    document.getElementById('toggle2').style.display='none';
    state.score = 0;
    state.timer = 10;
    scoreYouGot.innerHTML = state.score;
    document.getElementById('validationCustom05').value = null;
    
}

function init() {
    selectedWordSize.innerHTML = getWordSize.options[document.getElementById('validationCustom05').selectedIndex].text;
    problemUpdate();
    ourFieldAnswer.value = "";
    ourFieldAnswer.focus();
    //ourFieldAnswer.addEventListener("input", handleInput);
}
//to get the selected word size array
function generateSelactedAnagramArray() {
    let s = Number(getWordSize.options[document.getElementById('validationCustom05').selectedIndex].value);
    //console.log(s)
    let selectedArrayAnagram = json2array(jsonData);
   // console.log(selectedArrayAnagram[s])
    return selectedArrayAnagram[s];
}
function json2array(json) {
    var result = [];
    var keys = Object.keys(json);
    keys.forEach(function (key) {
      result.push(json[key]);
    });
    return result;
}
/**/
function questionArray() {
    let ran = randInt(0, generateSelactedAnagramArray().length - 1);
    //this.index = this.generateSelactedAnagramArray.findIndex(word => word === this.generateSelactedAnagramArray[ran]);
    return generateSelactedAnagramArray()[ran];
}
function getRandQuestion() {
    let L = questionArray().length;
    let anagramQuestionArray = questionArray()[randInt(0, L - 1)]; //random quations array
    let questionLength = L - 1;
    let questionWord = anagramQuestionArray;
    return { questionWord, questionLength };
}
function problemGenerate() {
    //var answersArray = [];
    let question = getRandQuestion();
    return question
}
function problemUpdate() {
    state.currentProblem = problemGenerate();
    problemElement.innerHTML = state.currentProblem.questionWord;
    reamingAnswer.innerHTML = state.currentProblem.questionLength
    ourFieldAnswer.value = "";
    ourFieldAnswer.focus();

}
function handleInput(e) {
    e.preventDefault()// remove default keyboard behavior
}