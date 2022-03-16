import { useEffect, useRef, useState } from "react";

function App() {
  const [count, setCount] = useState(0);
  const [output, setOutput] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const guessRef = useRef();
  const responseRef = useRef();

  useEffect(() => {
    if (count !== 0) {
      console.log("use effect triggerec..");
      const guessVal = guessRef.current.value;
      const responseVal = responseRef.current.value;
      setIsLoading(true);
      fetch("https://wordle-helper-app.herokuapp.com/suggestion", {
        method: "POST",
        body: JSON.stringify({
          guess_word: guessVal,
          guess_word_result: responseVal,
          iteration: count,
          word_list: output,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          setOutput(data.suggestion_result);
          setIsLoading(false);
        })
        .catch((err) => {
          console.log(err);
          setIsLoading(false);
        });
    }
  }, [count]);

  const onSubmitHandler = (event) => {
    event.preventDefault();
    setCount(count + 1);
  };

  return (
    <div>
      <form onSubmit={onSubmitHandler}>
        <label>Enter the guess: </label>
        <input type="text" ref={guessRef}></input>
        <label>Enter the response from wordle:</label>
        <input type="text" ref={responseRef}></input>
        <button type="submit">Submit</button>
      </form>
      <p>Guess No. : {count}</p>
      {!isLoading && output && output.map(e => <p>{e}</p>)}
      {isLoading && <p>Processing...</p>}
    </div>
  );
}

export default App;