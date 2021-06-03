import { makeStyles } from "@material-ui/core/styles";
import "App.css";

const useStyles = makeStyles((theme) => ({
  //mobile

  mobileContainer: {
    // overflow: 'auto',å
    height: "auto",
    position: "relative",
  },
  // TextTitleComponent
  mobileTitleBox: {
    margin: "10px",
  },
  mobileTitleText: {
    fontWeight: "bold",
    fontSize: "21px",
  },
  mobileSubtitleText: {
    color: "rgba(165, 147, 224, 1)",
    fontSize: "3.7vw",
  },

  //UploadImageComponent
  mobileEmptyImageBox: {
    height: "180px",
    backgroundColor: "var(--color-bg-light)",
    borderRadius: "15px",
    justifyContent: "center",
    alignContent: "center",
    outline: "none",
  },
  mobileInput: {
    display: " none",
  },
  mobileEmptyImageIcon: {
    color: "var(--color-bg-dark)",
    fontSize: "35px",
  },
}));

export { useStyles };
