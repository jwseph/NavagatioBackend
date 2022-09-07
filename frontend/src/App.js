import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import TripList from './layout/TripList';
import Signup from './pages/Signup';
import Login from './pages/Home';
import SearchBar from './components/SearchBar';

import './App.css';

function App() {
  return (
      <Routes>
        <Route element={<Login />}/>
        <Route path="/" element={<Nav />}>
          <Route index element={<Home/>}/>
        </Route>
      </Routes>
  );
}

export default App;
