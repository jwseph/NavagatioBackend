import { useState } from "react";
import { useSignup } from "../hooks/useSignup";
import { MdMail, MdLock } from 'react-icons/md';
import { AiFillEyeInvisible, AiFillEye} from 'react-icons/ai';

import ButtonList from '../layout/ButtonList';
import '../sass/button.scss';
import styles from "../sass/style/Auth.module.scss";

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
            <h1 className={styles.h1}>Welcome Back!</h1>
            <p>Log in you little bitch</p>
                <form onSubmit={handleSubmit}>
                    <div className={styles.form_container}>
                        <div className={styles.input_field}>
                            <MdMail className={styles.icon}/>
                            <div className={styles.content_field}>
                                <input className={styles.input} type="text" name="email" onChange={(event)=>{setEmail(event.target.value)}} required/>
                                <span className={styles.highlight}></span>
                                <label className={styles.label}>Email</label>
                            </div>
                        </div>

                        <div className={styles.input_field}>
                            <MdLock className={styles.icon}/>
                            <div className={styles.content_field}>
                                <input type={visibility?"text":"password"} onChange={(event)=>{setPassword(event.target.value)}} required/>
                                <span className={styles.highlight}></span>
                                <label>Password</label>
                                {visibility?<AiFillEye className={styles.eyecon} onClick={toggleVision}/>:<AiFillEyeInvisible className="eye_con" onClick={toggleVision}/>}
                            </div>
                        </div>

                        <div className={styles.flavor_container}>
                            <p>No account?<span style={{marginLeft: '0.5rem'}}>Sign up</span></p>
                            <p>Forgot password?</p>
                        </div>
                    </div>
                    <input type="submit" value="Log in" className={`${styles.btn} ${styles.btn_gray}`}/>
                    {error && <p>{error}</p>}
                </form>
            <div>
                <span/><p>or</p><span/>
            </div>
            <ButtonList/>
        </div>
    )
}