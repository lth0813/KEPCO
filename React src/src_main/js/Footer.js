import React, {Component} from "react";

class Footer extends Component {
    render() {
        return(
            <footer>
                <h5>{this.props.footer[0].text}</h5>
                <h5>{this.props.footer[1].text}</h5>
                <h5>{this.props.footer[2].text}</h5>
                <h5>{this.props.footer[3].text}</h5>
                <h5>{this.props.footer[4].text}</h5>
            </footer>
        )
    }
}

export default Footer;