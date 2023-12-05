import React, { Component } from 'react';

class Content extends Component {
    render() {
        return(
            <content>
                <h1 onClick={this.props.onChangePage}>{this.props.title}</h1>
                <h3>{this.props.desc}</h3>
            </content>
        )
    }
}
export default Content;
