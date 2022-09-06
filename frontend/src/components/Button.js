import '../sass/button.scss';
function Button(props) {
    return(
        <a href="#" className={ `btn ${props.theme}` }>{props.children}</a>
    )
}

export default Button