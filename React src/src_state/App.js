import React, {Component} from "react";
import Content from "./Content";
import Subject from "./Subject";
import TOC from "./TOC";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mode:"read",
      welcome:{title:"Welcome",desc:"Hello React"},
      contents:[{title:"HTML",desc:"HTML is for information"}],
      subject:{href:"#",title:"Web"},
      list:[
        {id:1, title:"HTML",url:"#1",desc:"HTML is for information"},
        {id:2, title:"CSS",url:"#2",desc:"CSS is for design"},
        {id:3, title:"JavaScript",url:"#3",desc:"JavaScript is for interactive"},],
      selected_id:1
    }
  }
  render() {
    let title, desc;
    if (this.state.mode === "welcome") {
      title = this.state.welcome.title;
      desc = this.state.welcome.desc;
    } else if (this.state.mode === "read") {
      title = this.state.contents[0].title;
      desc = this.state.contents[0].desc;
    }
    return(
      <div className="App">
        <Subject 
        href={this.state.subject.href} 
        title={this.state.subject.title}
        onEvent={()=>alert("title click")}/>
        <Content
        title={title}
        desc={desc}
        onChangePage={function() {this.setState({mode:"welcome"})}.bind(this)}
        />
        <TOC 
        list={this.state.list}
        onSelect={function() {this.setState({mode:"read"})}.bind(this)}
        />
      </div>
    )
  }
}
export default App