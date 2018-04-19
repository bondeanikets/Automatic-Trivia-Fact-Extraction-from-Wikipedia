// We have used the basic javascript model for quiz game from this website and modified it to fetch our own data.
// http://www.flashbynight.com/tutes/mcqquiz/ (Quiz Template)


$(document).ready(function () {
	$('#header').load('header.html');
	var questionNumber=0;
	var questionBank=new Array();
	var stage="#game1";
	var stage2=new Object;
	var questionLock=false;
	var numberOfQuestions;
	var score=0;
	var difficulty="easy";
	var diffSelected = false;
	var gameSelection=0;
	selectGame();

	function fetchQuestion(){
		if(gameSelection==1){
			url = "https://opentdb.com/api.php?amount=5&difficulty="+difficulty
		}else{
			url = "/questions"
		}
		$.get( url, function( data ) {
			var questions = data["results"];
			for(i=0;i<questions.length;i++){
				questionBank[i] = new Array;
				questionBank[i][0] = questions[i]["question"];
				questionBank[i][1]= questions[i]["correct_answer"];
				for(j=0; j<questions[i]["incorrect_answers"].length;j++){
					questionBank[i][j+2]= questions[i]["incorrect_answers"][j];
				}
			}
			numberOfQuestions=questionBank.length;
			displayQuestion();
		})
	}

	function selectDifficulty(){
		$(stage).append('<div class="questionText">'+"Select Difficulty Level"+'</div><div id="1" class="option">'+"Easy"+'</div><div id="2" class="option">'+"Medium"+'</div><div id="3" class="option">'+"Hard"+'</div>');
		$('.option').click(function(){
			difficulty = this.innerText;
			difficulty= difficulty.toLowerCase();
			changeSlide();
			fetchQuestion();
		})
	}

	function selectGame(){
		$(stage).append('<div class="questionText">'+"Select Game Type"+'</div><div id="1" class="option">'+"Quiz"+'</div><div id="2" class="option">'+"Learning Game"+'</div>');
		$('.option').click(function(){
			gameSelection = this.id;
			changeSlide();
			if(gameSelection==1){
				selectDifficulty();
			}else{
				fetchQuestion();
			}
		})
	}

	function displayQuestion(){
		var numberOfoptions = questionBank[questionNumber].length-1;

		var rnd=Math.random()*numberOfoptions;
		rnd=Math.ceil(rnd);
		var optionHtml = '';
		var optionList = [];
		var indexList = [];
		for(j=1; j<=numberOfoptions;j++){
			optionList.push(j);
			indexList.push(j);
		}
		optionList.splice(optionList.indexOf(1),1);
		var i=0;
		for(j=0;j<numberOfoptions;j++){
			if(j==rnd-1){
				indexList[j]=1;
			}else{
				indexList[j]=optionList[i];
				i++;
			}
		}

		for(i = 1; i<=numberOfoptions; i++){
			optionHtml = optionHtml+'<div id="'+i+'" class="option">'+questionBank[questionNumber][indexList[i-1]]+'</div>';
		}

		$(stage).append('<div class="questionText">'+questionBank[questionNumber][0]+'</div>'+optionHtml);
		// alert(questionBank[questionNumber][1]); -- To check answer uncomment this.
		$('.option').click(function(){
			if(questionLock==false){
				questionLock=true;	
		  		//correct answer
		  		if(this.id==rnd){
		  			$(stage).append('<div class="feedback1">CORRECT</div>');
		  			score++;
		  		}
		  		//wrong answer	
		  		if(this.id!=rnd){
		  			$(stage).append('<div class="feedback2">WRONG</div>');
		  		}
		  		setTimeout(function(){changeQuestion()},1000);
		  	}
		  })
	}

	//Function to handle for change to next question.
	function changeQuestion(){
		questionNumber++;
		if(stage=="#game1"){
			stage2="#game1";
			stage="#game2";
		}
		else{
			stage2="#game2";
			stage="#game1";
		}

		if(questionNumber<numberOfQuestions){
			displayQuestion();
		}
		else{
			displayFinalSlide();
		}
		
		$(stage2).animate({"right": "+=800px"},"slow", function() {
			$(stage2).css('right','-800px');
			$(stage2).empty();
		});
		$(stage).animate({"right": "+=800px"},"slow", function() {
			questionLock=false;
		});
	}

	//Function to change from one menu to another -- From game selection to question/ difficulty level selection menu.
	function changeSlide(){
		if(stage=="#game1"){
			stage2="#game1";
			stage="#game2";
		}
		else{
			stage2="#game2";
			stage="#game1";
		}
		$(stage2).animate({"right": "+=800px"},"slow", function() {
			$(stage2).css('right','-800px');
			$(stage2).empty();
		});
		$(stage).animate({"right": "+=800px"},"slow", function() {
			questionLock=false;
		});
	}

	//display final slide with results.
	function displayFinalSlide(){
		$(stage).append('<div class="questionText">You have finished the quiz!<br><br>Total questions: '+numberOfQuestions+'<br>Correct answers: '+score+'</div>');
		$(stage).append('<form action="game.html"><input type="submit"value="Restart" style="float: right; width:25%; height:inherit;" class="btn btn-primary" id = "search" /></form>')
	}
});//doc ready