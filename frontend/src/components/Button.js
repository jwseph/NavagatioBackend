import '../sass/button.scss';
function Button(props) {
    return(
        <a href="#" className='btn btn-gray'>{props.children}</a>
    )
}

export default Button