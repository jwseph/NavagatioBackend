import React, { useState, useEffect } from 'react';
// import TripList from './layout/TripList';
import Signup from './pages/Signup';
import Login from './pages/Login';
import SearchBar from './components/SearchBar';

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
      {/* <Login/> */}
      <SearchBar/>
    </div>
  );
}

export default App;
