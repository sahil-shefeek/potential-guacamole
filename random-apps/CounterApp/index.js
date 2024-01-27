let count = 0;
let step = 1;

document.getElementById("upcounterBtn").onclick = function () {
  count += step;
  document.getElementById("countLbl").textContent = count;
};

document.getElementById("downcounterBtn").onclick = function () {
  count -= step;
  document.getElementById("countLbl").textContent = count;
};

document.getElementById("resetBtn").onclick = function () {
  count = 0;
  document.getElementById("countLbl").textContent = count;
};

document.getElementById("updateSettings").onclick = function () {
  step = Number(document.getElementById("steps").value);
};

document.getElementById("resetSettings").onclick = function () {
  step = 0;
  document.getElementById("steps").value = "";
};
