import React, { useState, useEffect, Fragment } from 'react';
import './App.css';
import attractions from './baller.json';
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

  console.log(attractions)
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

    <h2>Attractions</h2>
    <ul>
          {
            attractions.map((attraction, i)  => {
              return <li key={i}>{attraction.basic_info.candidates[0].name} <br/> Rating: {attraction.basic_info.candidates[0].rating}</li>
            })
          }
    </ul>
    
    </div>
  );
}

export default App;
