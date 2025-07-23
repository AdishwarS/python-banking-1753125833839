package com.mycompany.myapp.web.rest;

import com.mycompany.myapp.service.UserService;
import com.mycompany.myapp.service.dto.UserDTO;
import java.util.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class PublicUserResource {

    private static final Logger LOG = LoggerFactory.getLogger(PublicUserResource.class);

    private final UserService userService;

    public PublicUserResource(UserService userService) {
        this.userService = userService;
    }

    /**
     * {@code GET /users} : get all users with only public information - calling this method is allowed for anyone.
     */
    @GetMapping("/users")
    public List<UserDTO> getAllPublicUsers() {
        return userService.getAllPublicUsers();
    }
}
