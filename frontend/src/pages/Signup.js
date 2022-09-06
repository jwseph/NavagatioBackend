import { useState } from "react";
import { useSignup } from "../hooks/useSignup";
import { MdMail, MdLock, MdFacebook,  } from 'react-icons/md';
import { FcGoogle} from 'react-icons/fc';
import { AiFillEyeInvisible, AiFillEye, AiFillApple } from 'react-icons/ai';

import Button from '../components/Button';
import '../sass/button.scss';
import "./Auth.scss";

export default function Signup() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [visibility, setVisibility] = useState(false)
    const { error, signup } = useSignup()

    const handleSubmit = (event) => {
        event.preventDefault()
        signup(email, password)
    }

    const toggleVision = () => {
        setVisibility(!visibility)
    }

    return(
        <div>
            <h1>Get Started</h1>
            <p>Please create an account by email</p>
                <form method="post" onSubmit={handleSubmit}>
                    <div className="form-container">
                        <div className="input-field">
                            <MdMail className="icon"/>
                            <div className="content-field">
                                <input type="text" name="email" onChange={(event)=>{setEmail(event.target.value)}} required/>
                                <span className="highlight"></span>
                                <label>Email</label>
                            </div>
                        </div>

                        <div className="input-field">
                            <MdLock className="icon"/>
                            <div className="content-field">
                                <input type={visibility?"text":"password"} onChange={(event)=>{setPassword(event.target.value)}} required/>
                                <span className="highlight"></span>
                                <label>Password</label>
                                {visibility?<AiFillEye className="eye-con" onClick={toggleVision}/>:<AiFillEyeInvisible className="eye-con" onClick={toggleVision}/>}
                            </div>
                        </div>

                        <div className="input-field">
                            <MdLock className="icon"/>
                            <div className="content-field">
                                <input type={visibility?"text":"password"} required/>
                                <span className="highlight"></span>
                                <label>Confirm password</label>
                                {visibility?<AiFillEye className="eye-con" onClick={toggleVision}/>:<AiFillEyeInvisible className="eye-con" onClick={toggleVision}/>}
                            </div>
                        </div>
                    </div>
                    <p>Already have an account?<span>Log in</span></p>
                    <input type="submit" value="Submit" className="btn btn-gray"/>
                    {error && <p>{error}</p>}
                </form>
            <div>
                <span/><p>or</p><span/>
            </div>
            <div className="button-container">
                <Button theme='btn-white'><FcGoogle/>Continue with Google</Button>
                <Button theme='btn-black'><AiFillApple/>Continue with Apple</Button>
                <Button theme='btn-blue'><MdFacebook/>Continue with Facebook</Button>
            </div>
        </div>
    )
}