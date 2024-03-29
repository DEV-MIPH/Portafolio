/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package vista;
    

import java.awt.Color;
import controlador.conexionUsuario;
import java.awt.event.KeyEvent;

import vista.admin;

/**
 *
 * @author miguel pereira
 */
import javax.swing.JComponent;
public class lobby extends javax.swing.JFrame {

    int xMouse, yMouse;
    String user,pass;
    boolean conectar;
    
    public lobby() {
        initComponents();
    }
    

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        buttonGroup1 = new javax.swing.ButtonGroup();
        bg = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        txtUser = new javax.swing.JTextField();
        jLabel6 = new javax.swing.JLabel();
        jSeparator1 = new javax.swing.JSeparator();
        jLabel3 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        txtPassword = new javax.swing.JPasswordField();
        bnbLogin = new javax.swing.JPanel();
        loginBtnTxt = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        jSeparator2 = new javax.swing.JSeparator();
        jSeparator3 = new javax.swing.JSeparator();
        jPanel2 = new javax.swing.JPanel();
        exitBtn = new javax.swing.JPanel();
        exitTxt = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("lobby");
        setLocationByPlatform(true);
        setUndecorated(true);
        setResizable(false);

        bg.setBackground(new java.awt.Color(255, 255, 255));
        bg.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel1.setFont(new java.awt.Font(".AppleSystemUIFont", 1, 36)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(0, 0, 0));
        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setText("Consulta Fonoaudiología ");
        bg.add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 30, 730, 70));

        jLabel4.setFont(new java.awt.Font(".AppleSystemUIFont", 0, 30)); // NOI18N
        jLabel4.setForeground(new java.awt.Color(0, 0, 0));
        jLabel4.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel4.setText("INICIAR SESIÓN ");
        bg.add(jLabel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 130, 730, 50));

        jLabel5.setFont(new java.awt.Font(".AppleSystemUIFont", 0, 18)); // NOI18N
        jLabel5.setForeground(new java.awt.Color(0, 0, 0));
        jLabel5.setText("Usuario:");
        bg.add(jLabel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(240, 200, 220, 30));

        txtUser.setBackground(new java.awt.Color(255, 255, 255));
        txtUser.setFont(new java.awt.Font("Roboto Light", 0, 14)); // NOI18N
        txtUser.setForeground(new java.awt.Color(0, 0, 0));
        txtUser.setBorder(null);
        txtUser.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                txtUserMousePressed(evt);
            }
        });
        txtUser.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtUserActionPerformed(evt);
            }
        });
        txtUser.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyPressed(java.awt.event.KeyEvent evt) {
                txtUserKeyPressed(evt);
            }
        });
        bg.add(txtUser, new org.netbeans.lib.awtextra.AbsoluteConstraints(240, 230, 220, 20));

        jLabel6.setFont(new java.awt.Font(".AppleSystemUIFont", 0, 18)); // NOI18N
        jLabel6.setForeground(new java.awt.Color(0, 0, 0));
        jLabel6.setText("Contraseña:");
        bg.add(jLabel6, new org.netbeans.lib.awtextra.AbsoluteConstraints(240, 270, 220, 30));
        bg.add(jSeparator1, new org.netbeans.lib.awtextra.AbsoluteConstraints(60, 260, -1, -1));

        jLabel3.setBackground(new java.awt.Color(255, 102, 102));
        jLabel3.setFont(new java.awt.Font(".AppleSystemUIFont", 1, 14)); // NOI18N
        jLabel3.setForeground(new java.awt.Color(69, 106, 196));
        jLabel3.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel3.setText("Hecho por IAGG");
        bg.add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(540, 480, 190, 47));

        jLabel2.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel2.setIcon(new javax.swing.ImageIcon(getClass().getResource("/images/logo-duoc.png"))); // NOI18N
        bg.add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 420, 190, 80));

        jLabel8.setFont(new java.awt.Font("Roboto Light", 1, 15)); // NOI18N
        jLabel8.setForeground(new java.awt.Color(255, 255, 255));
        jLabel8.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel8.setText("Escuela de Informática");
        bg.add(jLabel8, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 490, 190, 40));

        txtPassword.setBackground(new java.awt.Color(255, 255, 255));
        txtPassword.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        txtPassword.setForeground(new java.awt.Color(0, 0, 0));
        txtPassword.setBorder(null);
        txtPassword.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                txtPasswordMousePressed(evt);
            }
        });
        txtPassword.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtPasswordActionPerformed(evt);
            }
        });
        txtPassword.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyPressed(java.awt.event.KeyEvent evt) {
                txtPasswordKeyPressed(evt);
            }
        });
        bg.add(txtPassword, new org.netbeans.lib.awtextra.AbsoluteConstraints(240, 300, 220, 20));

        bnbLogin.setBackground(new java.awt.Color(255, 255, 255));
        bnbLogin.setForeground(new java.awt.Color(255, 255, 255));
        bnbLogin.setToolTipText("");

        loginBtnTxt.setFont(new java.awt.Font(".AppleSystemUIFont", 1, 14)); // NOI18N
        loginBtnTxt.setForeground(new java.awt.Color(0, 0, 0));
        loginBtnTxt.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        loginBtnTxt.setText("Entrar");
        loginBtnTxt.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        loginBtnTxt.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        loginBtnTxt.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                loginBtnTxtMouseClicked(evt);
            }
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                loginBtnTxtMouseEntered(evt);
            }
            public void mouseExited(java.awt.event.MouseEvent evt) {
                loginBtnTxtMouseExited(evt);
            }
            public void mousePressed(java.awt.event.MouseEvent evt) {
                loginBtnTxtMousePressed(evt);
            }
        });

        javax.swing.GroupLayout bnbLoginLayout = new javax.swing.GroupLayout(bnbLogin);
        bnbLogin.setLayout(bnbLoginLayout);
        bnbLoginLayout.setHorizontalGroup(
            bnbLoginLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, bnbLoginLayout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(loginBtnTxt, javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE))
        );
        bnbLoginLayout.setVerticalGroup(
            bnbLoginLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, bnbLoginLayout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(loginBtnTxt, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        loginBtnTxt.getAccessibleContext().setAccessibleName("");

        bg.add(bnbLogin, new org.netbeans.lib.awtextra.AbsoluteConstraints(240, 340, 120, 40));

        jLabel10.setIcon(new javax.swing.ImageIcon(getClass().getResource("/images/fondo1.png"))); // NOI18N
        bg.add(jLabel10, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 420, 870, 110));
        bg.add(jSeparator2, new org.netbeans.lib.awtextra.AbsoluteConstraints(240, 320, 240, 10));
        bg.add(jSeparator3, new org.netbeans.lib.awtextra.AbsoluteConstraints(240, 250, 240, 10));

        jPanel2.setBackground(new java.awt.Color(204, 204, 204));
        jPanel2.addMouseMotionListener(new java.awt.event.MouseMotionAdapter() {
            public void mouseDragged(java.awt.event.MouseEvent evt) {
                jPanel2MouseDragged(evt);
            }
        });
        jPanel2.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                jPanel2MousePressed(evt);
            }
        });

        exitBtn.setBackground(new java.awt.Color(204, 204, 204));
        exitBtn.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                exitBtnMouseEntered(evt);
            }
        });

        exitTxt.setBackground(new java.awt.Color(204, 204, 204));
        exitTxt.setFont(new java.awt.Font("Roboto Light", 1, 24)); // NOI18N
        exitTxt.setForeground(new java.awt.Color(0, 0, 0));
        exitTxt.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        exitTxt.setText("x");
        exitTxt.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        exitTxt.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                exitTxtMouseClicked(evt);
            }
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                exitTxtMouseEntered(evt);
            }
            public void mouseExited(java.awt.event.MouseEvent evt) {
                exitTxtMouseExited(evt);
            }
        });

        javax.swing.GroupLayout exitBtnLayout = new javax.swing.GroupLayout(exitBtn);
        exitBtn.setLayout(exitBtnLayout);
        exitBtnLayout.setHorizontalGroup(
            exitBtnLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(exitBtnLayout.createSequentialGroup()
                .addComponent(exitTxt, javax.swing.GroupLayout.PREFERRED_SIZE, 37, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, Short.MAX_VALUE))
        );
        exitBtnLayout.setVerticalGroup(
            exitBtnLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, exitBtnLayout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(exitTxt, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        jLabel7.setFont(new java.awt.Font("Chalkboard", 1, 13)); // NOI18N
        jLabel7.setForeground(new java.awt.Color(0, 0, 0));
        jLabel7.setText("FonoIA");

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel7, javax.swing.GroupLayout.PREFERRED_SIZE, 84, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 597, Short.MAX_VALUE)
                .addComponent(exitBtn, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(exitBtn, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addComponent(jLabel7, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        bg.add(jPanel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 730, 30));

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(bg, javax.swing.GroupLayout.PREFERRED_SIZE, 724, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(bg, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void txtUserActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtUserActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtUserActionPerformed

    private void jPanel2MousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jPanel2MousePressed
        xMouse = evt.getX();
        yMouse = evt.getY();
    }//GEN-LAST:event_jPanel2MousePressed

    private void jPanel2MouseDragged(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jPanel2MouseDragged
        int x = evt.getXOnScreen();
        int y = evt.getYOnScreen();
        this.setLocation(x-xMouse, y-yMouse);
    }//GEN-LAST:event_jPanel2MouseDragged

    private void exitTxtMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_exitTxtMouseClicked
        System.exit(0);
    }//GEN-LAST:event_exitTxtMouseClicked

    private void exitTxtMouseEntered(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_exitTxtMouseEntered
        exitBtn.setBackground(Color.red);
        exitTxt.setForeground(Color.white);
        
    }//GEN-LAST:event_exitTxtMouseEntered

    private void exitBtnMouseEntered(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_exitBtnMouseEntered
        
    }//GEN-LAST:event_exitBtnMouseEntered

    private void exitTxtMouseExited(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_exitTxtMouseExited
        exitBtn.setBackground(new Color(204,204,204));
        exitTxt.setForeground(Color.BLACK);
    }//GEN-LAST:event_exitTxtMouseExited

    private void loginBtnTxtMouseEntered(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_loginBtnTxtMouseEntered
        bnbLogin.setBackground(new Color(69,106,196));
        
    }//GEN-LAST:event_loginBtnTxtMouseEntered

    private void loginBtnTxtMouseExited(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_loginBtnTxtMouseExited
        bnbLogin.setBackground(Color.WHITE);
    }//GEN-LAST:event_loginBtnTxtMouseExited

    private void txtUserMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_txtUserMousePressed
//        if (txtUser.getText().equals("Ingrese su usuario...")){
//        txtUser.setText("");
//        txtUser.setForeground(Color.BLACK);
//        }
//        if(String.valueOf(txtPassword.getPassword()).isEmpty()){
//            txtPassword.setText("**********");
//            txtPassword.setForeground(Color.GRAY);
//        }
    }//GEN-LAST:event_txtUserMousePressed

    private void txtPasswordMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_txtPasswordMousePressed
//        if(String.valueOf(txtPassword.getPassword()).equals("**********")){
//            txtPassword.setText("");
//            txtPassword.setForeground(Color.BLACK);
//        }
//        if (txtUser.getText().isEmpty()){
//            txtUser.setText("Ingrese su usuario...");
//            txtUser.setForeground(Color.GRAY);
//        }
        
        
    }//GEN-LAST:event_txtPasswordMousePressed

    private void loginBtnTxtMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_loginBtnTxtMouseClicked
        
        
        
//        conectar = conexionUsuario.inicioSesion(user,pass);
//        user = conexionUsuario.usuario(user);
        
        
        
    }//GEN-LAST:event_loginBtnTxtMouseClicked

    private void loginBtnTxtMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_loginBtnTxtMousePressed
        user = txtUser.getText();
        pass = String.valueOf(txtPassword.getPassword());
        
        conectar =new conexionUsuario().inicioSesion(user,pass);
        if (conectar == true){
            javax.swing.JOptionPane.showMessageDialog(this, "Entrada Exitosa " + user , "LOGIN", javax.swing.JOptionPane.INFORMATION_MESSAGE);
            admin frmadministrador = new admin();
            frmadministrador.setVisible(true);
            this.setVisible(false);
            String nombreUsuario = new conexionUsuario().buscarNombre(user);
            admin.lblNombre.setText(nombreUsuario);
 
            
        }else{
            javax.swing.JOptionPane.showMessageDialog(this, "Intento de login con los datos:\nUsuario: " + user , "LOGIN", javax.swing.JOptionPane.INFORMATION_MESSAGE);
        }
    }//GEN-LAST:event_loginBtnTxtMousePressed

    private void txtPasswordKeyPressed(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtPasswordKeyPressed
        if(evt.getKeyCode()==KeyEvent.VK_ENTER){
            user = txtUser.getText();
            pass = String.valueOf(txtPassword.getPassword());
        
            conectar =new conexionUsuario().inicioSesion(user,pass);
            if (conectar == true){
                javax.swing.JOptionPane.showMessageDialog(this, "Entrada Exitosa " + user , "LOGIN", javax.swing.JOptionPane.INFORMATION_MESSAGE);
                admin frmadministrador = new admin();
                frmadministrador.setVisible(true);
                this.setVisible(false);
                String nombreUsuario = new conexionUsuario().buscarNombre(user);
                admin.lblNombre.setText(nombreUsuario);
            }else{
            javax.swing.JOptionPane.showMessageDialog(this, "Intento de login con los datos:\nUsuario: " + user , "LOGIN", javax.swing.JOptionPane.INFORMATION_MESSAGE);
            }
        }  
    }//GEN-LAST:event_txtPasswordKeyPressed

    private void txtUserKeyPressed(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtUserKeyPressed
//        if(evt.getKeyCode()==KeyEvent.VK_TAB){
//            if (txtUser.getText().equals("Ingrese su usuario...")){
//                txtUser.setText("");
//                txtUser.setForeground(Color.BLACK);
//            }
//            if(String.valueOf(txtPassword.getPassword()).isEmpty()){
//                txtPassword.setText("**********");
//                txtPassword.setForeground(Color.GRAY);
//            }
//        }
    }//GEN-LAST:event_txtUserKeyPressed

    private void txtPasswordActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtPasswordActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtPasswordActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(lobby.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(lobby.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(lobby.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(lobby.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new lobby().setVisible(true);
            }
        });
    }
    
 

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JPanel bg;
    private javax.swing.JPanel bnbLogin;
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JPanel exitBtn;
    private javax.swing.JLabel exitTxt;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JSeparator jSeparator2;
    private javax.swing.JSeparator jSeparator3;
    private javax.swing.JLabel loginBtnTxt;
    private javax.swing.JPasswordField txtPassword;
    private javax.swing.JTextField txtUser;
    // End of variables declaration//GEN-END:variables
}
