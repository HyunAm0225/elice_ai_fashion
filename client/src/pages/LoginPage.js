import React, { useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import { Mobile } from "../MediaQuery";
import { Box, TextField, Button } from "@material-ui/core";
import useStyles from "../styles/AuthPageStyle";
import Navbar from "../components/common/Navbar";
import swal from "sweetalert";

function LoginPage() {
  const classes = useStyles();
  const url = `http://elice-kdt-ai-track-vm-ai-14.koreacentral.cloudapp.azure.com:8000`;
  const history = useHistory();
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");

  const onChangeHandler = (event) => {
    const {
      target: { name, value },
    } = event;

    if (name === "id") {
      setId(value);
    } else if (name === "password") {
      setPassword(value);
    }
  };

  // 로그인 버튼 핸들러
  const onLoginHandler = (event) => {
    event.preventDefault();
    console.log("버튼누름!");
    axios
      .post(url + "/api/login/", {
        username: id,
        password: password,
        withCredentials: true,
      })
      .then((response) => {
        console.log(response);
        if (response.status === 201) {
          swal({
            title: "로그인 성공!",
            icon: "success",
          });
          history.push({
            pathname: "/main",
          });
        } else if (response.status === 401) {
          swal({
            title: "로그인 실패",
            text: "가입하지 않은 아이디이거나, 잘못된 비밀번호입니다.",
            icon: "error",
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
            <br />
            <Button
              className={classes.mobileButton}
              variant="contained"
              onClick={onLoginHandler}
            >
              로그인
            </Button>
          </Box>
          <Box className={classes.mobileButtonBox}>
            <Button
              className={classes.mobileButton}
              variant="contained"
              onClick={() => {
                history.push({ pathname: "/register" });
              }}
            >
              회원가입
            </Button>
          </Box>
        </form>
      </Box>
    </Mobile>
  );
}

export default LoginPage;
