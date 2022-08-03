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
const ErrorMassage = document.querySelector(".error-massage");
const AnswerButton = document.querySelector(".Answer_button");
// ---------Form data Input-------------------
const word_sizeData = document.querySelector('#id_word_size')
const score_Data = document.querySelector('#id_score')
const pointData = document.querySelector('#id_point')
const rankedData = document.querySelector('#id_ranked')  
//json 
var jsonData = JSON.parse(document.getElementById('element_id').textContent);
//console.log(jsonData)

//global variables
let state = { timeLeft: 0, score: 1, timer: 60, isPlaying: 1 , answersArray:[]}


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
    state.timer = 30;
    scoreYouGot.innerHTML = state.score;
    //re-starter
    starter();
    cleanTable();
}
//remove overlay-is-open css from body
//reset all classes, variables, and input fields
function resetOperatorGameToPlay(){
    document.body.classList.remove("overlay-is-open");
    document.getElementById('start2').style.display='block';
    //document.getElementById('ownGameScore').style.display='block';
    document.getElementById('toggle2').style.display='none';
    state.score = 0;
    state.timer = 30;
    scoreYouGot.innerHTML = state.score;
    document.getElementById('validationCustom05').value = null;   
    cleanTable();
}

function init() {
    selectedWordSize.innerHTML = getWordSize.options[document.getElementById('validationCustom05').selectedIndex].text;
    problemUpdate();
    ourFieldAnswer.value = "";
    ourFieldAnswer.focus();
    //ourFieldAnswer.addEventListener("keypress", handleInput);
    ourFieldAnswer.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
          // code for enter
          handleInput(e);
        }
    });
    AnswerButton.addEventListener('click', function (e) {
        // code for enter
        handleInput(e);
    });
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
function updateInput() {
    ourFieldAnswer.value = "";
    ourFieldAnswer.focus();
}

function questionArray() {
    let ran = randInt(0, generateSelactedAnagramArray().length - 1);
    //this.index = this.generateSelactedAnagramArray.findIndex(word => word === this.generateSelactedAnagramArray[ran]);
    return generateSelactedAnagramArray()[ran];
}
function getRandQuestion() {
    let questionArrayList = questionArray()
    let L = questionArrayList.length;
    let anagramQuestionArray = questionArrayList[randInt(0, L - 1)]; //random quations array
    let questionLength = L - 1;
    let questionWord = anagramQuestionArray;
    return { questionWord, questionLength ,questionArrayList};
}
function problemGenerate() {
    updateInput();
    state.answersArray = [];
    let question = getRandQuestion();
    state.answersArray.push(question.questionWord);
    return question ;
}
function problemUpdate() {
    state.currentProblem = problemGenerate();
    state.answersArray = [];
    problemElement.innerHTML = state.currentProblem.questionWord;
    reamingAnswer.innerHTML = state.currentProblem.questionLength
    updateInput();
    return state.currentProblem ;
}
function handleInput(e) {
    e.preventDefault()// remove default keyboard behavior
    if (ourFieldAnswer.value) {
        let answer = String(ourFieldAnswer.value).toLowerCase();
            //console.log(answer)
        if (state.currentProblem.questionLength>=1) {
                let correct = checkInput(
                    answer,
                    state.currentProblem.questionArrayList,
                    state.currentProblem.questionWord
              );
              //console.log(correct);
            if (correct) {
                let notRepted = checkInput(
                    answer,
                    state.answersArray,
                    state.currentProblem.questionWord
                );
                if (!notRepted) {
                    state.score++; 
                    scoreYouGot.innerHTML = state.score;
                    state.currentProblem.questionLength--;
                    reamingAnswer.innerHTML = state.currentProblem.questionLength;
                    state.answersArray.push(answer);
                    console.log(state.answersArray)
                    
                    insertTable(answer)
                    updateInput();
                }
            } else {
                updateInput();
                console.log("updateInput(wrowing answer)");
            }
        } else {
                cleanTable();
                problemUpdate();
                console.log("updateInput(RestWord===2)");
        }
    } else {
        ErrorMassage.innerHTML = "you must enter answer!!";
    }
}
function checkInput(input, questionArrayWords, questionWord) {
    if (input === questionWord.toLowerCase()) { 
        return false;
    }
    else { 
        return questionArrayWords.some((ArrayWords) =>input.toLowerCase().includes(ArrayWords.toLowerCase()));
    }
}
        
  
// dynamic function to create table from arrays
function insertTable(tableData) {
    let tableBody = document.querySelector("#correct-answer");
    const tr = document.createElement('tr');
    const content = `<td ><i class="bi bi-check2-square px-1"></i>${tableData}</td> `;
    tr.innerHTML = content;
    tableBody.appendChild(tr)
}
  
//dynamic function to delete table
function cleanTable() {
    $(".table_correct > tbody").empty();
}
  
