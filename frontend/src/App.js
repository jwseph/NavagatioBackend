import React, { useState, useEffect } from 'react';
// import TripList from './layout/TripList';
import Auth from './layout/Auth';

import './App.css';

function App() {
  // useEffect(() => {
  //   fetch("/search/Muki").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setKismet(data)
  //       console.log(data);
  //     }
  //   )
  // }, [])

  // console.log(attractions)
  return (
    <div className="App">
      <Auth/>
    </div>
  );
}

export default App;
