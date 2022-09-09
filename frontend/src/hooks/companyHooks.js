import { useState } from 'react';
import { getAuth, signInWithRedirect, GoogleAuthProvider, OAuthProvider, FacebookAuthProvider,  } from "firebase/auth";


export const useGoogleLogin = () => {
    const provider = new GoogleAuthProvider();
    const auth = getAuth();
    console.log('Click');
    signInWithRedirect(auth, provider);
}
