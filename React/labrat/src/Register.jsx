import React, { useState } from "react";

export const Register = (props) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault(); // prevents page from refreshing
        console.log('username: ', username);
    }

    return (
        <div className="auth-form-container">
            <h1>Register</h1>
            <form className= "register-form" onSubmit={handleSubmit}>
                <label htmlFor="username">Username</label>
                <input value={username} onChange={(e) => setUsername(e.target.value)}type="text" placeholder= "Username" id="username" name="username" />
                <label htmlFor="password">Password</label>
                <input type="password" placeholder= "********" id="password" name="password" />
                <button type="submit"> Register</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('login')}>Log In</button>
        </div>
    );
}