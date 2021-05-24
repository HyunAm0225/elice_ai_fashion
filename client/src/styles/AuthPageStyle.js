import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  mobileAuthBox: {
    height: "91vh",
    width: "100%",
    display: "flex",
    justifyContent: "center",
  },
  mobileTextField: {
    margin: "0.5vw",
  },
  mobileInputBox: {
    height: "63.9vh",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
  },
  mobileTextBox: {
    height: "63.9vh",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },
  mobileControlBox: {
    height: "10vh",
  },
  mobileTitle: {
    fontWeight: "bold",
  },
  mobileMessage: {
    width: "70vw",
  },
  mobileButtonBox: {
    height: "26.1vh",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
  },
  mobileButton: {
    width: "70vw",
    borderRadius: "15px",
  },
}));

export default useStyles;
