import React, { useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import { Mobile } from "../MediaQuery";
import { Box, TextField, Button } from "@material-ui/core";
import useStyles from "../styles/AuthPageStyle";
import Navbar from "../components/common/Navbar";
import swal from "sweetalert";

axios.defaults.withCredentials = true;

function RegisterPage() {
  const classes = useStyles();
  const url = `http://elice-kdt-ai-track-vm-ai-14.koreacentral.cloudapp.azure.com:8000`;
  const history = useHistory();
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");
  const [passwordCheck, setPasswordCheck] = useState("");
  const [name, setName] = useState("");

  // (회원가입 폼) 입력 핸들러
  const onChangeHandler = (event) => {
    const {
      target: { name, value },
    } = event;

    if (name === "id") {
      setId(value);
    } else if (name === "password") {
      setPassword(value);
    } else if (name === "passwordCheck") {
      setPasswordCheck(value);
    } else if (name === "name") {
      setName(value);
    }
  };

  // 회원가입 버튼 핸들러
  const onSignUpHandler = (event) => {
    event.preventDefault();
    console.log("버튼누름!");
    if (password === passwordCheck) {
      console.log(id);
      axios
        .post(url + "/api/signup/", {
          username: id,
          password: password,
          email: "test324212@test.com",
          full_name: name,
          withCredentials: true,
        })
        .then((response) => {
          console.log(response);
          if (response.status === 201) {
            swal({
              title: "회원가입 성공!",
              icon: "success",
            });
            history.push({
              pathname: "/register/closet",
            });
          } else if (response.status === 301) {
            swal({
              title: "회원가입 실패",
              text: "필수 입력 사항이 모두 입력되지 않았습니다.",
              icon: "warning",
            });
          } else if (response.data.status === 302) {
            swal({
              title: "회원가입 실패",
              text: "이미 등록된 이메일 주소입니다.",
              icon: "warning",
            });
          } else if (
            response.data.username === "이미 존재하는 아이디 입니다."
          ) {
            swal({
              title: "회원가입 실패",
              text: "이미 등록된 별명입니다.",
              icon: "warning",
            });
          } else if (response.data.status === 304) {
            swal({
              title: "회원가입 실패",
              text: "비밀번호 기준에 맞지 않습니다. 비밀번호는 8자이상, 숫자+영어+특수문자 조합으로 이루어집니다.",
              icon: "warning",
            });
          } else if (response.data.status === 305) {
            swal({
              title: "회원가입 실패",
              text: "비밀번호는 하나이상의 특수문자가 들어가야합니다.",
              icon: "warning",
            });
          } else {
            console.log(response.data);
            alert("error");
          }
        })
        .catch((error) => {
          console.log(error);
          swal({
            title: "에러발생",
            text: "예상치 못한 오류가 발생했습니다",
            icon: "warning",
          });
        });
    }
  };

  return (
    <Mobile>
      <Navbar />
      <Box className={classes.mobileAuthBox}>
        <form>
          <Box className={classes.mobileInputBox}>
            <TextField
              className={classes.mobileTextField}
              id="standard-basic"
              label="아이디를 입력해주세요."
              name="id"
              type="text"
              value={id}
              onChange={onChangeHandler}
              required
            />
            <TextField
              className={classes.mobileTextField}
              id="standard-basic"
              label="비밀번호를 입력해주세요."
              name="password"
              type="password"
              value={password}
              onChange={onChangeHandler}
              required
            />
            <TextField
              className={classes.mobileTextField}
              error={passwordCheck && password !== passwordCheck ? true : false}
              id="standard-basic"
              label={
                passwordCheck && password !== passwordCheck
                  ? "비밀번호가 일치하지 않습니다."
                  : "비밀번호를 확인해주세요."
              }
              name="passwordCheck"
              type="password"
              value={passwordCheck}
              onChange={onChangeHandler}
              required
            />
            <TextField
              className={classes.mobileTextField}
              id="standard-basic"
              label="이름을 입력해주세요."
              name="name"
              type="text"
              value={name}
              onChange={onChangeHandler}
              required
            />
          </Box>
          <Box className={classes.mobileButtonBox}>
            <Button
              className={classes.mobileButton}
              variant="contained"
              onClick={onSignUpHandler}
            >
              가입하기
            </Button>
          </Box>
        </form>
      </Box>
    </Mobile>
  );
}

export default RegisterPage;
