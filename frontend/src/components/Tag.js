import style from './Tag.module.css';
import {useState} from 'react';
const Tag = (props) => {
    const [clicked, setClicked] = useState(false)
    const theme = props.theme
    
    function handleClick() {
        setClicked(!clicked)  
    }

    return(
        <span className={style.tag} onClick={handleClick} style={{backgroundColor:clicked?theme.colors_light[props.index]:theme.colors[props.index]}}>
            {props.children}
        </span>
    )
}

export default Tag