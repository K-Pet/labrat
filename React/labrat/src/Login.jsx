import React, { useState } from 'react';

export const Login = (props) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault(); // prevents page from refreshing
        console.log('username: ', username);
    }


  return (
      <div className="auth-form-container">
        <h1>Log In</h1>
        <form className= "login-form" onSubmit={handleSubmit}>
            <label htmlFor="username">Username</label>
            <input value={username} onChange={(e) => setUsername(e.target.value)}type="text" placeholder= "Username" id="username" name="username" />
            <label htmlFor="password">Password</label>
            <input type="password" placeholder= "********" id="password" name="password" />
            <button type="submit"> Log In</button>
        </form>
        <button className="link-btn" onClick={() => props.onFormSwitch('register')}>Register</button>
      </div>
    )
}