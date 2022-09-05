import Button from '../components/Button';
const Login = () => {
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
                <p>Don't have an account?<span>Sign up</span></p>
                <Button>Log In</Button>
                {error && <p>{error}</p>}
            </form>
        </div>
    )
}