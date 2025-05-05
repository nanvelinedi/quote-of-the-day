import React, { useState } from 'react';

function App() {
  const [quote, setQuote] = useState('');

  const fetchQuote = async () => {
    const res = await fetch('https://your-flask-api.onrender.com/quote');
    const data = await res.json();
    setQuote(data.quote);
  };

  return (
    <div className="App">
      <h1>Quote of the Day</h1>
      <button onClick={fetchQuote}>Get Quote</button>
      <p>{quote}</p>
    </div>
  );
}

export default App;
