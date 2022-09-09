import Button from '../components/Button';
import { useGoogleLogin } from '../hooks/companyHooks';
import {  MdFacebook } from 'react-icons/md';
import { FcGoogle} from 'react-icons/fc';
import { AiFillApple } from 'react-icons/ai';

const ButtonList = () => {

  return(
    <div className="button-container">
      <Button theme='btn-white' onClick={useGoogleLogin}><FcGoogle className='button-icon'/>Continue with Google</Button>
      <Button theme='btn-black'><AiFillApple className='button-icon'/>Continue with Apple</Button>
      <Button theme='btn-blue'><MdFacebook className='button-icon'/>Continue with Facebook</Button>
    </div>
  )
}

export default ButtonList