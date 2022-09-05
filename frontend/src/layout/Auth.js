import { useState } from "react";
import { useSignup } from "../hooks/useSignup"

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
                <form action="POST" onSubmit={handleSubmit}>
                    <div className="wrapper-field">
                        <span>Email</span>
                        <input type="text" name="email" required=""/>
                    </div>
                    
                    <input type="password" name="" required="" placeholder="Password"/>
                    <p>Already have an account?<span>Sign in</span></p>
                    <button>Sign Up</button>
                    {error && <p>{error}</p>}
                </form>
        </div>
    )
}