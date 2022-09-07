import { useState } from "react";
import { useSignup } from "../hooks/useSignup";
import { MdMail, MdLock } from 'react-icons/md';
import { AiFillEyeInvisible, AiFillEye} from 'react-icons/ai';

import ButtonList from '../layout/ButtonList';
import '../sass/button.scss';
import "../sass/style/Auth.module.scss";

export default function Signup() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')


    const [visibility, setVisibility] = useState(false)
    const { error, signup } = useSignup()

    const handleSubmit = (event) => {
        event.preventDefault()
        signup(email, password)
        console.log('submit');
    }

    const toggleVision = () => {
        setVisibility(!visibility)
    }

    return(
        <div className="center">
            <h1>Get Started</h1>
            <p>Please create an account by email</p>
                <form onSubmit={handleSubmit} className="form-container">
                    <div>
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
                                {visibility?<AiFillEye className="eyecon" onClick={toggleVision}/>:<AiFillEyeInvisible className="eyecon" onClick={toggleVision}/>}
                            </div>
                        </div>

                        <div className="input-field">
                            <MdLock className="icon"/>
                            <div className="content-field">
                                <input type={visibility?"text":"password"} required/>
                                <span className="highlight"></span>
                                <label>Confirm password</label>
                                {visibility?<AiFillEye className="eyecon" onClick={toggleVision}/>:<AiFillEyeInvisible className="eyecon" onClick={toggleVision}/>}
                            </div>
                        </div>
                    </div>
                    <div className="flavor-container">
                            <p>Already have an account?<span style={{marginLeft: '0.5rem'}}>Log in</span></p>
                    </div>
                    <input type="submit" value="Sign up" className="btn btn-gray"/>
                    {error && <p>{error}</p>}
                </form>
                <p>or</p>
            <ButtonList/>
        </div>
    )
}