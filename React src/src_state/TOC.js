import React, {Component} from "react";

class TOC extends Component {
    render() {
        let lists = [];
        let data = this.props.list;
        for (let i = 0; i < data.length; i++) {
            lists.push(<a href={data[i].url} onClick={this.props.onSelect}><li>{data[i].title}</li></a>)
        }
        return(
            <toc>
                <ul>
                    {lists}
                </ul>
            </toc>
        )
    }
}

export default TOC;