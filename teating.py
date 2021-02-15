CREATE TABLE IF NOT EXISTS `employee` (
  `emp_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_name` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `phone` varchar(100) NOT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

INSERT INTO `employee` (`emp_id`, `emp_name`, `email`, `phone`) VALUES
(1, 'John', 'john@example.com', '2323234543'),
(2, 'Smith', 'smith@example.com', '9898577442'),
(3, 'Priska', 'priska@example.com', '9393452387'),
(4, 'Gaga', 'gaga@example.com', '8482764537');
