import React, { useState, useEffect } from 'react';
import TripList from './Layout/TripList';

import './App.css';

function App() {
  const [kismet, setKismet] = useState([{}])

  useEffect(() => {
    fetch("/search/Muki").then(
      res => res.json()
    ).then(
      data => {
        setKismet(data)
        console.log(data);
      }
    )
  }, [])

  // console.log(attractions)
  return (
    <div className="App">
      <h1>Welcome to Wanderlag</h1>
      <TripList/>
      <p>Bruh</p>
    {/* <h2>Attractions</h2>
    <ul>
          {
            attractions.map((attraction, i)  => {
              return <li key={i}>{attraction.basic_info.candidates[0].name} <br/> Rating: {attraction.basic_info.candidates[0].rating}</li>
            })
          }
    </ul> */}
    
    </div>
  );
}

export default App;
