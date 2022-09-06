import Button from '../components/Button';
import {  MdFacebook } from 'react-icons/md';
import { FcGoogle} from 'react-icons/fc';
import { AiFillApple } from 'react-icons/ai';

const ButtonList = () => {
  return(
    <div className="button-container">
      <Button theme='btn-white'><FcGoogle/>Continue with Google</Button>
      <Button theme='btn-black'><AiFillApple/>Continue with Apple</Button>
      <Button theme='btn-blue'><MdFacebook/>Continue with Facebook</Button>
    </div>
  )
}

export default ButtonList