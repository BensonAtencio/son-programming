window.onload = sendApiRequest

async function sendApiRequest(){
  let response = await fetch('https://opentdb.com/api.php?amount=10&category=9&type=multiple')
  console.log(response)
  let data = await response.json()
  console.log(data)
  useApiData(data)
}

function useApiData(data){
  document.getElementById("#category").innerHTML = `Category: ${data.results[0].category}`
  document.getElementById("#difficulty").innerHTML = `Difficult: ${data.results[0].difficulty}`
  document.getElementById("#question").innerHTML = `Question: ${data.results[0].question}`
  document.getElementById("#answer1").innerHTML = data.results[0].correct_answer
}