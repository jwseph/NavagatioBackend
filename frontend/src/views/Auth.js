import { useState } from "react";
import { useSignup } from "../hooks/useSignup"

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
            <h2>
                <form action="POST" onSubmit={handleSubmit}>
                    <label>
                        <span>Email:</span>
                        <input 
                            required 
                            type="email" 
                            onChange={(event)=>setEmail(event.target.value)} 
                            value={email}
                        />
                    </label>
                    <label>
                        <span>Password:</span>
                        <input 
                            required 
                            type="password" 
                            onChange={(event)=>setPassword(event.target.value)} 
                            value={password}
                        />
                    </label>
                    <button>Sign Up</button>
                    {error && <p>{error}</p>}
                </form>
            </h2>
        </div>
    )
}