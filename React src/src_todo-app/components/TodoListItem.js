import React from "react";
import { MdCheckBox, MdCheckBoxOutlineBlank, MdRemoveCircleOutline } from "react-icons/md";
import "../css/TodoListItem.css";

const TodoListItem = (props) => {
    const { id, text, checked, date } = props.todo;
    return (
        <div className="TodoListItem">
            <div className={checked ? 'checkbox checked' : 'checkbox'} onClick={() => props.onToggle(id)}>
                {checked ? <MdCheckBox/> : <MdCheckBoxOutlineBlank/>}
                <div className="text"><span class="left">{text}</span><span class="right">{date}</span></div>
            </div>
            <div className="remove" onClick={() => {props.onRemove(id);}}>
                <MdRemoveCircleOutline></MdRemoveCircleOutline>
            </div>
        </div>
    );
};

export default TodoListItem;