import { useState } from "react";
import { useSignup } from "../hooks/useSignup";
import { MdMail, MdLock } from 'react-icons/md';
import { AiFillEyeInvisible, AiFillEye} from 'react-icons/ai';

import ButtonList from '../layout/ButtonList';
import '../sass/button.scss';
import "../sass/style/Auth.scss";

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
        <div className="">
            <h1>Welcome Back!</h1>
            <p>Log in you little bitch</p>
                <form onSubmit={handleSubmit}>
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
                                {visibility?<AiFillEye className="eyecon" onClick={toggleVision}/>:<AiFillEyeInvisible className="eye-con" onClick={toggleVision}/>}
                            </div>
                        </div>

                        <div className="flavor-container">
                            <p>No account?<span style={{marginLeft: '0.5rem'}}>Sign up</span></p>
                            <p>Forgot password?</p>
                        </div>
                    </div>
                    <input type="submit" value="Log in" className="btn btn-gray"/>
                    {error && <p>{error}</p>}
                </form>
            <div>
                <span/><p>or</p><span/>
            </div>
            <ButtonList/>
        </div>
    )
}