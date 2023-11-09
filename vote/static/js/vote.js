const form = document.getElementById('poll-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const selectedOption = document.querySelector('input[name="language"]:checked').value;

  // Here, you can replace the console.log() statement
  // with the code to save the poll response to a database
  console.log(selectedOption);

  const totalVotes = 100; // this value can be retrieved from the database
  const votesPerOption = { Bola: 45, Peter: 35, Atiku: 20 }; // these values can be retrieved from the database as well
  const percentage = Math.round((votesPerOption[selectedOption] / totalVotes) * 100);

  resultDiv.innerHTML = `You voted for ${selectedOption}.<br>Percentage of votes: ${percentage}%`;
  form.reset();
});
