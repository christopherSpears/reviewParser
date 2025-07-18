# reviewParser
Product review export to XML parsed and converted to csv.

A large XML file was exported with several thousand product reviews. The task was to convert this file to a csv with a specified format. After converted to csv, email addresses were then looked up from a separate product review export and ported over. Once the emails were loaded, French reviews were identified and the locale was added to all rows. Then finally, the email was moved from the "email" column to the "User Email" column.
