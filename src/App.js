import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    console.log("Calling", process.env.REACT_APP_APIURL + '/time')
    axios.get(process.env.REACT_APP_APIURL + '/time').then(response => {
      console.log("API request SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p><a href="https://github.com/ScholliYT/heroku-cra-test">Heroku-cra-test</a> with flask api</p>
        <div>{getMessage.status === 200 ? 
          <h3>API time: {getMessage.data.time}</h3>
          :
          <h3>LOADING API call</h3>}</div>
      </header>
    </div>
  );
}

export default App;
