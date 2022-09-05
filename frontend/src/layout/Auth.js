import { useState } from "react";
import { useSignup } from "../hooks/useSignup";
import { MdMail, MdLock } from 'react-icons/md';
import { AiFillEyeInvisible } from 'react-icons/ai';

import "./Auth.scss"

export default function Auth() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const { error, signup } = useSignup()

    const handleSubmit = (event) => {
        event.preventDefault()
        signup(email, password)
    }

    return(
        <div>
            <h1>Get Started</h1>
            <p>Please create an account by email</p>
                <form method="post" onSubmit={handleSubmit}>
                    <div className="content-field">
                        <input type="text" name="email" onChange={(event)=>{setEmail(event.target.value)}} required/>
                        <span className="highlight"></span>
                        <label><MdMail className="icon"/>  Email</label>
                    </div>
                    
                    <div className="content-field">
                        <input type="password" onChange={(event)=>{setPassword(event.target.value)}} required/>
                        <span className="highlight"></span>
                        <label><MdLock/>  Password</label>
                    </div>

                    <div className="content-field">
                        <input type="password" required/>
                        <span className="highlight"></span>
                        <label><MdLock/>Confirm password</label> 
                    </div>
                    <p>Already have an account?<span>Sign in</span></p>
                    <button>Sign Up</button>
                    {error && <p>{error}</p>}
                </form>
        </div>
    )
}