import { makeStyles } from "@material-ui/core/styles";
import '../App.css';

const useStyles = makeStyles((theme) => ({
  //mobile

  mobileContainer: {
    // overflow: 'auto',å
    height: "auto",
    position: "relative",
  },
  mobileTitleBox: {
    margin: "10px",
  },
  mobileTitleText: {
    fontWeight: "bold",
    fontSize: "21px",
  },
  mobileSubtitleText: {
    color: "rgba(165, 147, 224, 1)",
    fontSize: "15px",
  },

  mobileClosetImageGrid: {
    padding: "10px",
  },

  mobileImageBox: {
    height: "180px",
    backgroundColor: "var(--color-bg-light)",
    borderRadius: "15px",
    borderColor: "black",
  },

  mobileImage: {
    objectFit: "cover",
    height: "100%",
    width: "100%",
    borderRadius: "15px",
  },

  mobileEmptyImageBox: {
    height: "180px",
    backgroundColor: "var(--color-bg-light)",
    borderRadius: "15px",
    justifyContent: "center",
    alignContent: "center",
    outline: "none",
  },
  mobileEmptyImageIcon: {
    color: "var(--color-bg-dark)",
    fontSize: "35px",
  },
  mobileInput: {
    display: " none",
  },
}));

export { useStyles };
