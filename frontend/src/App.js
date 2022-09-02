import React, { useState, useEffect, Fragment } from 'react';
import './App.css';
// import 'loading.png';
function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/trips").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data);
      }
    )
  }, [])

  return (
    <div className="App">
      <h1>Welcome to Wanderlag</h1>
      {(typeof data.top_trips === 'undefined') ? (
        <Fragment>
          <p>Loading...</p>
          <img src="images/loading.png" className='loading'/>
        </Fragment>
      ): (
        <ul>
          {
            data.top_trips.map((trip , i) => (
              <li key={i}>{trip}</li>
            ))
          }
        </ul>
      )}

    </div>
  );
}

export default App;
