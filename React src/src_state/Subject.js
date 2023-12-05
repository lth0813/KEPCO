import React, {Component} from "react";

class Subject extends Component {
    render() {
        return(
            <header>
                <a href={this.props.href} 
                onClick={()=>{this.props.onEvent()}}
                >
                    <h1>{this.props.title}</h1>
                </a>
            </header>
        )
    }
}

export default Subject;