const restartGameToPlayButton = document.querySelector('.reset_button');
const scoreYouGot = document.querySelector(".score_result");
const gameStarterButton = document.querySelector('.operator-btn');
const TimeLeftCounter = document.querySelector(".Time-left");
const resetOperator = document.querySelector(".resetOperator")
const resultEndMessage = document.querySelector(".end-message");
const fineScoreResult = document.querySelector(".fine-score-result");
const saveScoreBtn = document.querySelector('.save_score');
const selectedOperators = document.querySelector(".selected-operators");
//const gameExiting  = document.getElementById('exiting');
const selactedRange  = document.querySelector('.selected_num_range');
const buttonStart = document.getElementById('button_start');
const problemElement = document.querySelector(".problem");
const ourFieldAnswer = document.querySelector(".answer-input");
const getOperatorNumber = document.querySelector("#validationCustom04");
const getMaxRangeNumber = document.querySelector("#validationCustom03");
const updatingResult = document.querySelector('#scoreData');       
// ---------Screen Key Board-------------------
const allClearButton = document.querySelector('.input-value-clear');
const numberButtons = document.querySelectorAll('.input-value');
const currentOperandTextElement = document.querySelector('.answer-input');        

// ---------Form data Input-------------------
const operatorData = document.querySelector('#id_operator')
const max_rangeData = document.querySelector('#id_max_range')
const score_Data = document.querySelector('#id_score')
const pointData = document.querySelector('#id_point')
const rankedData = document.querySelector('#id_ranked')  
  
let state = {
    timeLeft: 0,
    score: 1,
    timer: 10,
    isPlaying: 1,
    
}

// generating and rendering the option for select from filed
$(function () {
    var $select = $(".selacted-rang");
    for (i = 1; i <= 100; i++) {
        $select.append($('<option></option>').val(i).html(i))
    }
});

// Example starter JavaScript for disabling form submissions if there are invalid fields
window.addEventListener('load',() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
    
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (form.checkValidity()) {
            //alert('1'+form.checkValidity())
            event.preventDefault()
            event.stopPropagation()
            gameLaunch();
            //getOption();
        }
        
        //alert('2'+form.checkValidity())
        form.classList.add('was-validated')
        
      }, true)
    })

  });

//buttonStart.addEventListener('click', getOption)
function gameLaunch(){
    document.getElementById('start').style.display='none';
    document.getElementById('ownGameScore').style.display='none';
    document.getElementById('toggle').style.display='block';
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
                let rang = Number(getMaxRangeNumber.options[document.getElementById('validationCustom03').selectedIndex].value)
                pointData.value = state.score * rang;
                rankedData.value = rang++;
                clearInterval(startGameTimer);
            } 
    }
}


    

  
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

}

function resetOperatorGameToPlay(){
    document.body.classList.remove("overlay-is-open");
    document.getElementById('start').style.display='block';
    document.getElementById('ownGameScore').style.display='block';
    document.getElementById('toggle').style.display='none';
    state.score = 0;
    state.timer = 30;
    scoreYouGot.innerHTML = state.score;
    document.getElementById('validationCustom04').value = null;
    document.getElementById('validationCustom03').value = null;
}
function init() {
    selectedOperators.innerHTML = getOperatorNumber.options[document.getElementById('validationCustom04').selectedIndex].text;
    selactedRange.innerHTML = getMaxRangeNumber.options[document.getElementById('validationCustom03').selectedIndex].text;
    let r = Number(selactedRange.innerHTML);
    //console.log(r);
    updateProblem();
    ourFieldAnswer.focus();
    ourFieldAnswer.addEventListener("input", handleInput);

}

function updateProblem() {
    state.currentProblem = generateProblem();
    if(state.currentProblem.operator === '/'){
        if(state.currentProblem.numberTwo == 0){state.currentProblem.numberTwo = 1}
        problemElement.innerHTML = `${state.currentProblem.numberOne} ${state.currentProblem.operator} ${state.currentProblem.numberTwo}`;

    } else{
        problemElement.innerHTML = `${state.currentProblem.numberOne} ${state.currentProblem.operator} ${state.currentProblem.numberTwo}`;

    }
    ourFieldAnswer.value = "";
    ourFieldAnswer.focus();

}

function generateProblem() {
    return {
                numberOne: generateNumber(),
                operator: ['+', '/', 'x', '-'][getSelectedOperator()],
                numberTwo: generateNumber()
    }
}    
    
function generateNumber() {
    const maximum = Number(getMaxRangeNumber.options[document.getElementById('validationCustom03').selectedIndex].value);
    max_rangeData.value = Number(getMaxRangeNumber.options[document.getElementById('validationCustom03').selectedIndex].value);
    //console.log(maximum)
    return Math.floor(Math.random() * (maximum + 1))
}
function getSelectedOperator() {
    let OperatorNumber = getOperatorNumber.options[document.getElementById('validationCustom04').selectedIndex].value;
    operatorData.value = getOperatorNumber.options[document.getElementById('validationCustom04').selectedIndex].text;
    return OperatorNumber;
}

function handleInput(e) {
    e.preventDefault()// remove default keyboard behavior

    let correctAnswer
    const p = state.currentProblem
    if (p.operator == "+") correctAnswer = p.numberOne + p.numberTwo;
    if (p.operator == "-") correctAnswer = p.numberOne - p.numberTwo;
    if (p.operator == "x") correctAnswer = p.numberOne * p.numberTwo;
    if (p.operator == "/") correctAnswer = Math.floor(p.numberOne / p.numberTwo);
            
    if (parseInt(ourFieldAnswer.value, 10) === correctAnswer) {
        state.score++;
        updateProblem();
        ourFieldAnswer.focus();

    } else {
        problemElement.classList.add("animate-wrong");
        setTimeout(() => problemElement.classList.remove("animate-wrong"), 451);
    }
    scoreYouGot.innerHTML = state.score;
   
}

// ------------------Screen Key Board------------------------

class ScreenKeyBoard {
    constructor(currentOperandTextElement) {
        this.currentOperandTextElement = currentOperandTextElement;
        this.clear();
    }
    clear() {
        this.currentOperand = '';
    }
    appendNumber(number) {
        this.currentOperand = this.currentOperand.toString() + number.toString();
    }
}

const screenKeyBoard = new ScreenKeyBoard(currentOperandTextElement);
numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        screenKeyBoard.appendNumber(button.innerText);
        screenKeyBoard.currentOperandTextElement.value = screenKeyBoard.currentOperand;
        let correctAnswer;
        const p = state.currentProblem;
        if (p.operator == "+") correctAnswer = p.numberOne + p.numberTwo;
        if (p.operator == "-") correctAnswer = p.numberOne - p.numberTwo;
        if (p.operator == "x") correctAnswer = p.numberOne * p.numberTwo;
        if (p.operator == "/") correctAnswer = Math.floor(p.numberOne / p.numberTwo);
           
        
        //check matched
        if (parseInt(screenKeyBoard.currentOperandTextElement.value, 10) === correctAnswer) {
            state.score++;
            updateProblem();
            screenKeyBoard.clear();
            ourFieldAnswer.focus();
        } else {
            problemElement.classList.add("animate-wrong");
            setTimeout(() => problemElement.classList.remove("animate-wrong"), 451);
        }
        scoreYouGot.innerHTML = state.score;
    });
});
allClearButton.addEventListener('click', () => {
    screenKeyBoard.clear();
    screenKeyBoard.currentOperandTextElement.value = screenKeyBoard.currentOperand;
});





