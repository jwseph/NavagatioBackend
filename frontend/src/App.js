import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import TripList from './layout/TripList';
import Signup from './pages/Signup';
import Login from './pages/Login';
// import Nav from './pages/Nav';
// import Home from './pages/Login'
import SearchBar from './components/SearchBar';
import './App.css';

function App() {
  const [authed, setAuthed] = useState(false);

  return (
      <Routes>
        <Route path="/signup" element={<Signup />}/>
        <Route path="/login" element={<Login />}/>
        {/* <Route path="/" element={<Nav />}>
          <Route index element={<Home/>}/>
        </Route> */}
      </Routes>
  );
}

export default App;
