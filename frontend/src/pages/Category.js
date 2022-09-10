import data from '../json/tags.json';
import Tag from '../components/Tag';

const Category = () => {
    const tag_themes = 
    {
        colors:['#28b485', '#ff7730', '#5643fa'],
        colors_light:['#55c57a', '#ffb900','#2998ff']
    }

    return(
        <p>
            {
                data.map((data, i) => {
                    const index = Math.floor(Math.random() * 3);
                    return(<Tag key={i} index={index} theme={tag_themes}>{data}</Tag>)
                })
            }
        </p>
    )
}

export default Category