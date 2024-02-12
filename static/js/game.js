const table = document.querySelector("#tblBingo");
const letter = document.querySelectorAll(".letters-bingo");
const startButton = document.getElementById("start-button");
const definitionElement = document.getElementById("definition");
const BINGO = document.getElementById("BINGO");
let cellToDefinition = {};
let winningIterator = 0;

startButton.addEventListener("click", function () {
  startButton.style.display = "none";
  BINGO.style.display = "block";
  BINGO.style.margin = "auto";
  //Timer and Progress bar
  let countDownDate = new Date().getTime() + 5 * 60 * 1000;
  let totalDuration = 5 * 60 * 1000;
  let timer = setInterval(function () {
    let now = new Date().getTime();
    let distance = countDownDate - now;

    let progress = 100 * (distance / totalDuration);
    document.getElementById("progressBarContainer").style.display = "block";
    document.getElementById("progressBar").style.width = progress + "%";

    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);
    let milliseconds = distance % 1000;

    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;
    milliseconds = milliseconds < 10 ? "00" + milliseconds : milliseconds;

    document.getElementById("timer").textContent =
      minutes + ":" + seconds + ":" + milliseconds;

    if (distance < 0) {
      clearInterval(timer);
      document.getElementById("timer").textContent = "00:00:00";
      document.getElementById("progressBar").style.width = "0%";
      alert("Time OUT!!!");
      location.reload();
    }
  }, 1);

  //fetching the definition
  fetch("get-definitions/")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      console.log(1);
      definitions = data.definitions;
      let arr = Array.apply(null, { length: 26 }).map(Number.call, Number);

      arr.shift();
      shuffle(arr);
      console.log(arr);

      for (let i = 0; i < 25; i++) {
        cellToDefinition[arr[i].toString()] = definitions[i].word;
      }

      let divElement = document.createElement("div");
      let inputField = document.createElement("input");
      let submitButton = document.createElement("button");

      divElement.id = "submission";
      inputField.id = "input";
      submitButton.id = "Submit";
      submitButton.textContent = "Submit";

      divElement.appendChild(inputField);
      divElement.appendChild(submitButton);
      document.body.appendChild(divElement);

      submitButton.addEventListener("click", function () {
        let word = inputField.value;
        let cell = Array.from(
          document.querySelectorAll(".main-table-cell")
        ).find((cell) => cellToDefinition[cell.id] === word);

        if (cell && !cell.classList.contains("strickout")) {
          cell.classList.add("strickout");
          definitionElement.textContent = "Correct!";

          if (matchWin()) {
            letter[winningIterator].classList.add("show-bingo");
            winningIterator++;

            if (winningIterator === 5) {
              alert("bingo");
              location.reload();
            }
          }
        }
        inputField.value = "";
      });

      let iterator = 0;

      for (i = 0; i < 5; i++) {
        let tr = document.createElement("tr");
        table.appendChild(tr);
        for (j = 0; j < 5; j++) {
          let td = document.createElement("td");
          td.id = arr[iterator].toString();
          td.style.height = "20%";
          td.style.width = "20%";
          td.classList.add("main-table-cell");

          let div = document.createElement("div");
          div.classList.add("cell-format");
          div.textContent = arr[iterator].toString();
          td.appendChild(div);

          td.addEventListener("click", function () {
            let word = cellToDefinition[td.id];
            let definition = definitions.find((def) => def.word === word);
            if (definition) {
              definitionElement.textContent =
                definition.definition + " : " + definition.word;
            }
          });
          tr.appendChild(td);
          iterator++;
        }
      }
    });
});

const winningPosition = [
  [0, 1, 2, 3, 4],
  [5, 6, 7, 8, 9],
  [10, 11, 12, 13, 14],
  [15, 16, 17, 18, 19],
  [20, 21, 22, 23, 24],
  [0, 5, 10, 15, 20],
  [1, 6, 11, 16, 21],
  [2, 7, 12, 17, 22],
  [3, 8, 13, 18, 23],
  [4, 9, 14, 19, 24],
  [0, 6, 12, 18, 24],
  [4, 8, 12, 16, 20],
];

function shuffle(arr) {
  let currentIndex = arr.length,
    randomIndex;

  while (currentIndex != 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [arr[currentIndex], arr[randomIndex]] = [
      arr[randomIndex],
      arr[currentIndex],
    ];
  }

  return arr;
}

function matchWin() {
  const cell = document.querySelectorAll(".main-table-cell");
  return winningPosition.some((combination) => {
    let ite = 0;
    combination.forEach((index) => {
      if (cell[index].classList.contains("strickout")) ite++;
    });

    if (ite === 5) {
      let indexWin = winningPosition.indexOf(combination);
      winningPosition.splice(indexWin, 1);
    }

    return combination.every((index) => {
      return cell[index].classList.contains("strickout");
    });
  });
}
