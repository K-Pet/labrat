import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { Login } from './Login';
import { Register } from './Register';
import { HomePage } from './HomePage';
import { useNavigate } from 'react-router-dom';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function Auth() {
  const navigate = useNavigate();
  const [currentForm, setCurrentForm] = useState("login"); // ['login', 'register']

  const handleFormChange = (formName) => {
    setCurrentForm(formName);
  }
  
  return (
    <div className="App">
    {
      currentForm === "login" ? <Login onFormSwitch={handleFormChange} navigate={navigate}/> : <Register onFormSwitch={handleFormChange} navigate={navigate}/>
    }
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/home" element={<HomePage />} />
        <Route path="/*" element={<Auth />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;